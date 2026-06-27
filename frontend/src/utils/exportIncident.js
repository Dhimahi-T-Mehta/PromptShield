export const exportIncident = (attack) => {

    if (!attack) {
        alert("No incident selected.");
        return;
    }

    const headers = [
        "Field",
        "Value"
    ];

    const rows = [

        ["Timestamp", attack.timestamp],

        ["Prompt", attack.prompt],

        ["Attack Type", attack.attack_type
            ?.replace(/_/g, " ")
            .replace(/\b\w/g, c => c.toUpperCase())
        ],

        ["Confidence",
            `${Math.round(attack.confidence * 100)}%`
        ],

        ["Risk Score", attack.risk_score],

        ["Action", attack.action],

        ["Severity",
            attack.explanation?.severity || ""
        ],

        ["Detection Modules",
            (attack.explanation?.detection_modules || [])
                .join(", ")
        ],

        ["Matched Keywords",
            (attack.explanation?.matched_keywords || [])
                .join(", ")
        ],

        ["Detected Entities",
            (attack.explanation?.detected_entities || [])
                .join(", ")
        ],

        ["Recommended Action",
            attack.explanation?.recommended_action || ""
        ],

        ["Analyst Note",
            attack.explanation?.analyst_note || ""
        ]

    ];

    const csv = [

        headers,

        ...rows

    ]
        .map(row =>
            row
                .map(col =>
                    `"${String(col ?? "").replace(/"/g, '""')}"`
                )
                .join(",")
        )
        .join("\n");

    const blob = new Blob(
        [csv],
        { type: "text/csv;charset=utf-8;" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    const filenameTime = attack.timestamp
        .replace(/[: ]/g, "-");

    link.href = url;

    link.download =
        `incident_report_${filenameTime}.csv`;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);

};