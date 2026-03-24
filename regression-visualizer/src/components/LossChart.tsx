import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import useTrainingStore from "../store/store";

export default function LossChart() {
  const lossHistory = useTrainingStore((s) => s.lossHistory);

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={lossHistory}>
        <XAxis
          dataKey="epoch"
          label={{ value: "epoch", position: "insideBottom", offset: -2 }}
        />
        <YAxis />
        <Tooltip formatter={(v) => v.toFixed(6)} />
        <Line
          type="monotone"
          dataKey="loss"
          stroke="#7F77DD"
          dot={false}
          isAnimationActive={false} // critical — disable for live streaming
        />
      </LineChart>
    </ResponsiveContainer>
  );
}
