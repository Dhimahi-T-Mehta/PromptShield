export default function StatusBar() {

    const items = [

        "AI Engine Online",

        "Threat Detection Active",

        "JWT Auth Enabled",

        "Redis Connected",

    ];

    return (

        <div className="status-bar">

            {

                items.map((item) => (

                    <div
                        key={item}
                        className="status-item"
                    >

                        <span className="status-dot"></span>

                        {item}

                    </div>

                ))

            }

        </div>

    );

}