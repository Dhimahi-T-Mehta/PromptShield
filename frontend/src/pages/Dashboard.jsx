import { useEffect, useState } from "react";
import ThreatExplanation from "../components/ThreatExplanation";
import HeroSection from "../components/HeroSection";
import SystemStatus from "../components/SystemStatus";
import ThreatLevel from "../components/ThreatLevel";
import KPICards from "../components/KPICards";
import AttackDistribution from "../components/AttackDistribution";
import RequestChart from "../components/RequestChart";
import EventFeed from "../components/EventFeed";
import RecentAttacks from "../components/RecentAttacks";
import ThreatIntelCards from "../components/ThreatIntelCards";
import api from "../services/api";
import ThreatTrendChart from "../components/ThreatTrendChart";
import DetectionModuleStats from "../components/DetectionModuleStats";
import "../styles/dashboard.css";
import FilterBar from "../components/FilterBar";
import { exportToCSV } from "../utils/exportCSV";

function Dashboard() {

    const [overview, setOverview] = useState({
        total_requests: 0,
        blocked_requests: 0,
        allowed_requests: 0
    });

    const [loading, setLoading] = useState(true);
    
    const [moduleStats, setModuleStats] = useState(null);

    const [trendData, setTrendData] = useState([]);

    const [distribution, setDistribution] = useState([]);

    const [attacks, setAttacks] = useState([]);

    const [lastUpdated, setLastUpdated] = useState("");

    const [threatIntel, setThreatIntel] = useState(null);

    const [selectedAttack, setSelectedAttack] = useState(null);

    const [filters, setFilters] = useState({

    search: "",

    attackType: "all",

    action: "all",

    timeRange: "all",

});
    const fetchDashboardData = async () => {

        try {

            const [
                overviewRes,
                distributionRes,
                attacksRes,
                intelRes,
                trendRes,
                moduleRes
            ] = await Promise.all([
                api.get("/dashboard/overview"),
                api.get("/dashboard/attack-distribution"),
                api.get("/dashboard/recent-attacks"),
                api.get("/dashboard/threat-intelligence"),
                api.get("/dashboard/threat-trends"),
                api.get("/dashboard/detection-modules")
            ]);

            setOverview(
                overviewRes.data
            );

            setTrendData(trendRes.data);

            setModuleStats(moduleRes.data);

            setDistribution(

                Object.entries(
                    distributionRes.data
                ).map(
                    ([key, value]) => ({

                        name: key,

                        value: value

                    })
                )

            );

            setAttacks(
                attacksRes.data
            );

            setThreatIntel(
                intelRes.data
            );

            if (selectedAttack) {
                const updatedAttack = attacksRes.data.find(
                    (a) =>
                        a.timestamp === selectedAttack.timestamp &&
                        a.attack_type === selectedAttack.attack_type
                );

                if (updatedAttack) {
                    setSelectedAttack(updatedAttack);
                }
            }
            
            setLastUpdated(
                new Date().toLocaleTimeString()
            );

        }

        catch (error) {

            console.error(
                "Dashboard Error:",
                error
            );

        }

    };

useEffect(() => {

        fetchDashboardData();

        const interval = setInterval(
            fetchDashboardData,
            10000
        );

        return () => clearInterval(interval);

    }, []);


    // =====================================
    // KPI Calculations
    // =====================================

    const detectionRate =

        overview.total_requests > 0

            ? Number(

                (

                    overview.blocked_requests

                    /

                    overview.total_requests

                )

                * 100

            ).toFixed(1)

            : 0;           

const filteredAttacks = attacks.filter((attack) => {

    const searchTerm = filters.search.toLowerCase();

    const matchesSearch =

        searchTerm === "" ||

        (attack.attack_type ?? "")

            .toLowerCase()

            .includes(searchTerm) ||

        (attack.prompt ?? "")

            .toLowerCase()

            .includes(searchTerm);

    const matchesAttack =

        filters.attackType === "all" ||

        attack.attack_type === filters.attackType;

    const matchesAction =

        filters.action === "all" ||

        attack.action === filters.action;

    const attackDate = new Date(attack.timestamp);

    const today = new Date();

    const diffDays =
        (today - attackDate) /
        (1000 * 60 * 60 * 24);

    const matchesTime =

        filters.timeRange === "all" ||

        (filters.timeRange === "today" &&
            diffDays < 1) ||

        (filters.timeRange === "7days" &&
            diffDays <= 7) ||

        (filters.timeRange === "30days" &&
            diffDays <= 30);

            return (
            matchesSearch &&
            matchesAttack &&
            matchesAction &&
            matchesTime
        );

});

const filteredOverview = {

    total_requests: filteredAttacks.length,

    blocked_requests:

        filteredAttacks.filter(

            attack => attack.action === "BLOCK"

        ).length,

    allowed_requests:

        filteredAttacks.filter(

            attack => attack.action === "ALLOW"

        ).length,

};

const distributionCounts = filteredAttacks.reduce(

    (acc, attack) => {

        acc[attack.attack_type] =

            (acc[attack.attack_type] || 0) + 1;

        return acc;

    },

    {}

);

const filteredDistribution = Object.entries(

    distributionCounts

).map(

    ([name, value]) => ({

        name,

        value,

    })

);

useEffect(() => {
    if (!selectedAttack) return;
    const stillVisible = filteredAttacks.some(
        attack =>
            attack.timestamp === selectedAttack.timestamp
    );
    if (!stillVisible) {
        setSelectedAttack(null);
    }
}, [
    selectedAttack,
    filters,
    attacks,
]);
    return (

        <div className="dashboard">

            <HeroSection
    threatLevel={overview.threat_level}
    protectionScore={overview.protection_score}
    lastUpdated={lastUpdated}
/>

            <SystemStatus

                lastUpdated={lastUpdated}

            />

            <ThreatLevel

                detectionRate={Number(detectionRate)}

            />

      <KPICards
    totalRequests={overview.total_requests}
    blockedRequests={overview.blocked_requests}
    allowedRequests={overview.allowed_requests}
    detectionRate={detectionRate}
    protectionScore={overview.protection_score}
/>
           
    <ThreatIntelCards intelligence={threatIntel} />

        <FilterBar
            filters={filters}
            setFilters={setFilters}
            onExport={() => exportToCSV(filteredAttacks)}
        />

    
    <ThreatTrendChart
        data={trendData}

    />

        <DetectionModuleStats
            data={moduleStats}
        />

        <div className="charts-grid">

                <AttackDistribution

                    data={filteredDistribution}

                />

                <RequestChart
                    blocked={filteredOverview.blocked_requests}
                    allowed={filteredOverview.allowed_requests}
                />
            </div>

            <EventFeed

                attacks={filteredAttacks}

            />

            <div className="dashboard-bottom">

                <RecentAttacks
                    attacks={filteredAttacks}
                    selectedAttack={selectedAttack}
                    setSelectedAttack={setSelectedAttack}
                />

                <ThreatExplanation
                    attack={selectedAttack}
                />

            </div>

        </div>

    );

}

export default Dashboard;