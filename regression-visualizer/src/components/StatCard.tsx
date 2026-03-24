import useTrainingStore from "../store/store";

export default function StatCards() {
  const w = useTrainingStore((s) => s.w);
  const b = useTrainingStore((s) => s.b);
  const status = useTrainingStore((s) => s.status);

  return (
    <div style={{ display: "flex", gap: 16, marginBottom: 24 }}>
      <div style={cardStyle}>
        <div style={labelStyle}>w (weight)</div>
        <div style={valueStyle}>{w ?? "—"}</div>
        <div style={subStyle}>target ≈ 3.0</div>
      </div>
      <div style={cardStyle}>
        <div style={labelStyle}>b (bias)</div>
        <div style={valueStyle}>{b ?? "—"}</div>
        <div style={subStyle}>target ≈ 2.0</div>
      </div>
      <div style={cardStyle}>
        <div style={labelStyle}>status</div>
        <div style={valueStyle}>{status}</div>
      </div>
    </div>
  );
}

const cardStyle = {
  background: "#f5f5f5",
  borderRadius: 8,
  padding: "12px 20px",
  minWidth: 120,
};
const labelStyle = { fontSize: 12, color: "#888", marginBottom: 4 };
const valueStyle = { fontSize: 22, fontWeight: 500 };
const subStyle = { fontSize: 11, color: "#aaa", marginTop: 2 };
