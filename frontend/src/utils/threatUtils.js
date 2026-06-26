export function getThreatLevel(detectionRate) {
  if (detectionRate >= 80) return "CRITICAL";
  if (detectionRate >= 50) return "HIGH";
  if (detectionRate >= 20) return "MEDIUM";
  return "LOW";
}