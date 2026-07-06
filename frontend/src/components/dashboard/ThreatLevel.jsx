function ThreatLevel({ detectionRate }) {

  let level = "LOW";
  let className = "threat-low";

  if (detectionRate >= 80) {
    level = "CRITICAL";
    className = "threat-critical";
  } else if (detectionRate >= 50) {
    level = "HIGH";
    className = "threat-high";
  } else if (detectionRate >= 20) {
    level = "MEDIUM";
    className = "threat-medium";
  }

  return (
    <div className="threat-card">
      <h3>Threat Level</h3>

      <div className={`threat-badge ${className}`}>
        {level}
      </div>
    </div>
  );
}

export default ThreatLevel;