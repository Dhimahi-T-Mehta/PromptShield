function EventFeed({
  attacks,
}) {

 if(attacks.length===0){
      return(
        <div className="empty-state">
        📡
        <h3>No Recent Security Events</h3>
        <p>
        No security incidents match the current filters.
        </p>
        </div>
      )
  }


  const latest =
    attacks.slice(0, 5);

  return (
    <div className="feed-card">
      <h2>Live Event Feed</h2>

      <div className="timeline">
        {latest.map(
          (attack, index) => (
            <div
              key={index}
              className="timeline-item"
            >
              <div
              className={
                attack.action === "BLOCK"
                  ? "timeline-dot danger-dot"
                  : "timeline-dot success-dot"
              }
            />

              <div>
                <strong>
                  {attack.action}
                </strong>

                {" - "}

                {attack.attack_type
                  .replace(/_/g, " ")
                  .replace(/\b\w/g, (char) => char.toUpperCase())}

                <br />

                <small>
                  {
                    attack.timestamp
                  }
                </small>
              </div>
            </div>
          )
        )}
      </div>
    </div>
  );
}

export default EventFeed;