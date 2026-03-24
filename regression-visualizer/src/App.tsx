import useTrainingStore from "./store/store";
import StatCards from "./components/StatCard";
import LossChart from "./components/LossChart";

export default function App() {
  const lr = useTrainingStore((s) => s.lr);
  const status = useTrainingStore((s) => s.status);
  const setLr = useTrainingStore((s) => s.setLr);
  const startTraining = useTrainingStore((s) => s.startTraining);

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", padding: "0 24px" }}>
      <h2 style={{ marginBottom: 24 }}>Live training — linear regression</h2>

      <StatCards />

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 16,
          marginBottom: 24,
        }}
      >
        <label style={{ fontSize: 14 }}>Learning rate: {lr}</label>
        <input
          type="range"
          min={0.01}
          max={1.0}
          step={0.01}
          value={lr}
          onChange={(e) => setLr(parseFloat(e.target.value))}
          style={{ flex: 1 }}
        />
      </div>

      <button
        onClick={startTraining}
        disabled={status === "streaming"}
        style={{ marginBottom: 24, padding: "8px 20px" }}
      >
        {status === "streaming" ? "Training..." : "Start training"}
      </button>

      <LossChart />
    </div>
  );
}
