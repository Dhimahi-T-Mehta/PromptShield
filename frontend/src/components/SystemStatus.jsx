function SystemStatus({
  lastUpdated,
}) {
  return (
    <div className="status-card">

      <div className="status-indicator"></div>

      <span>
        System Online
      </span>

      <span className="updated-time">
        Updated:
        {lastUpdated}
      </span>

    </div>
  );
}

export default SystemStatus;