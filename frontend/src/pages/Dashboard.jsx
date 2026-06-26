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

import "../styles/dashboard.css";

function Dashboard() {

    const [overview, setOverview] = useState({
        total_requests: 0,
        blocked_requests: 0,
        allowed_requests: 0
    });

    const [distribution, setDistribution] = useState([]);

    const [attacks, setAttacks] = useState([]);

    const [lastUpdated, setLastUpdated] = useState("");

    const [threatIntel, setThreatIntel] = useState(null);

    const [selectedAttack, setSelectedAttack] = useState(null);

    useEffect(() => {

        fetchDashboardData();

        const interval = setInterval(
            fetchDashboardData,
            10000
        );

        return () => clearInterval(interval);

    }, []);

    const fetchDashboardData = async () => {

        try {

            const [
                    overviewRes,
                    distributionRes,
                    attacksRes,
                    intelRes
                ] = await Promise.all([
                    api.get("/dashboard/overview"),
                    api.get("/dashboard/attack-distribution"),
                    api.get("/dashboard/recent-attacks"),
                    api.get("/dashboard/threat-intelligence")
                ]);

            setOverview(
                overviewRes.data
            );

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

            <div className="charts-grid">

                <AttackDistribution

                    data={distribution}

                />

                <RequestChart

                    blocked={overview.blocked_requests}

                    allowed={overview.allowed_requests}

                />

            </div>

            <EventFeed

                attacks={attacks}

            />

            <div className="dashboard-bottom">

                <RecentAttacks
                    attacks={attacks}
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