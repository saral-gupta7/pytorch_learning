import { create } from "zustand";

const useTrainingStore = create((set, get) => ({
  status: "idle",
  lossHistory: [],
  w: null,
  b: null,
  lr: 0.1,

  // --- actions ---
  setLr: (lr) => set({ lr }),

  startTraining: () => {
    const { lr, status } = get();

    if (status === "streaming") return;

    set({ status: "streaming", lossHistory: [], w: null, b: null });

    const es = new EventSource(`http://localhost:8000/train?lr=${lr}`);

    es.onmessage = (event) => {
      const msg = JSON.parse(event.data);

      set((state) => ({
        lossHistory: [...state.lossHistory, msg],
        w: msg.w,
        b: msg.b,
      }));

      // Training complete
      if (msg.epoch === 99) {
        set({ status: "done" });
        es.close();
      }
    };

    es.onerror = () => {
      set({ status: "idle" });
      es.close();
    };
  },
}));

export default useTrainingStore;
