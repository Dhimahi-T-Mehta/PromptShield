export const exportToCSV = (attacks) => {

    if (!attacks.length) {
        alert("No incidents to export.");
        return;
    }

    const headers = [
        "Timestamp",
        "Prompt",
        "Attack Type",
        "Confidence",
        "Risk Score",
        "Action",
        "Severity",
        "Detection Modules",
        "Matched Keywords"
    ];

    const rows = attacks.map((attack) => ([
        attack.timestamp,
        attack.prompt,
        attack.attack_type,
        attack.confidence,
        attack.risk_score,
        attack.action,
        attack.explanation?.severity || "",
        (attack.explanation?.detection_modules || []).join(", "),
        (attack.explanation?.matched_keywords || []).join(", ")
    ]));

    const csvContent = [
        headers,
        ...rows
    ]
        .map(row =>
            row
                .map(value => `"${String(value ?? "").replace(/"/g, '""')}"`)
                .join(",")
        )
        .join("\n");

    const blob = new Blob(
        [csvContent],
        { type: "text/csv;charset=utf-8;" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    const now = new Date();

    const timestamp =
        now.toISOString()
            .replace(/:/g, "-")
            .replace("T", "_")
            .split(".")[0];

    link.href = url;

    link.download = `promptshield_incidents_${timestamp}.csv`;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);
};