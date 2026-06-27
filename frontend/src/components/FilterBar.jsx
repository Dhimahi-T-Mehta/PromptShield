import "./FilterBar.css";

function FilterBar({
    filters,
    setFilters,
    onExport,
}) {

    const handleChange = (e) => {

        setFilters({

            ...filters,

            [e.target.name]: e.target.value,

        });

    };

    return (

        <div className="filter-container">

            <input
                type="text"
                name="search"
                placeholder="🔍 Search prompt or attack..."
                value={filters.search}
                onChange={handleChange}
            />

            <select
                name="attackType"
                value={filters.attackType}
                onChange={handleChange}
            >

                <option value="all">All Attacks</option>
                <option value="safe">Safe</option>
                <option value="prompt_injection">Prompt Injection</option>
                <option value="jailbreak">Jailbreak</option>
                <option value="pii_extraction">PII Extraction</option>
                <option value="role_manipulation">Role Manipulation</option>

            </select>

            <select
                name="action"
                value={filters.action}
                onChange={handleChange}
            >

                <option value="all">All Actions</option>
                <option value="ALLOW">ALLOW</option>
                <option value="BLOCK">BLOCK</option>

            </select>

            <select
                name="timeRange"
                value={filters.timeRange}
                onChange={handleChange}
            >

                <option value="all">All Time</option>

                <option value="today">Today</option>

                <option value="7days">Last 7 Days</option>

                <option value="30days">Last 30 Days</option>

            </select>
            <div className="filter-actions">
            <button
                className="export-btn"
                onClick={onExport}
            >
                ⬇ Export CSV
            </button>

            <button
                className="reset-btn"
                onClick={() =>
                    setFilters({

                        search: "",

                        attackType: "all",

                        action: "all",

                        timeRange: "all",

                    })
                }

            >

                Reset

            </button>
        </div>
        </div>

    );

}

export default FilterBar;