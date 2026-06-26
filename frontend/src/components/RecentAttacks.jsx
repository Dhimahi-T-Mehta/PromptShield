const getAttackClass = (
  attackType
) => {
  switch (attackType) {
    case "safe":
      return "safe-tag";

    case "prompt_injection":
      return "prompt-tag";

    case "jailbreak":
      return "jailbreak-tag";

    case "pii_extraction":
      return "pii-tag";

    case "role_manipulation":
      return "role-tag";

    default:
      return "";
  }
};

const getRiskLevel = (
  risk
) => {
  if (risk >= 90)
    return "critical";

  if (risk >= 70)
    return "high";

  if (risk >= 40)
    return "medium";

  return "low";
};

const formatAttackType = (attackType) => {
  return attackType
    .replace(/_/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
};

function RecentAttacks({

    attacks,

    selectedAttack,

    setSelectedAttack

})
 {
  return (
    <div className="table-card">
      <h2>Recent Attacks</h2>

      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Attack Type</th>
            <th>Confidence</th>
            <th>Risk</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {attacks.map(
            (attack, index) => {
              const level =
                getRiskLevel(
                  attack.risk_score
                );

              return (
                <tr
                    key={index}
                    onClick={() => setSelectedAttack(attack)}
                    className={
                        selectedAttack === attack
                            ? "selected-row"
                            : ""
                    }
                >
                  <td>
                    {
                      attack.timestamp
                    }
                  </td>

                  <td>
                  <span
                    className={getAttackClass(
                      attack.attack_type
                    )}
                  >
                    {
                      formatAttackType(
                        attack.attack_type
                      )
                    }
                  </span>
                </td>
                  <td>
                    {Math.round(attack.confidence * 100)}%
                  </td>

                  <td>
                    <span
                      className={`risk-badge ${level}`}
                    >
                      {level.toUpperCase()}
                    </span>
                  </td>

                  <td>
                    <span
                      className={
                        attack.action ===
                        "BLOCK"
                          ? "block-tag"
                          : "allow-tag"
                      }
                    >
                      {
                        attack.action
                      }
                    </span>
                  </td>
                </tr>
              );
            }
          )}
        </tbody>
      </table>
    </div>
  );
}

export default RecentAttacks;