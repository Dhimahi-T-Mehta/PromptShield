import { FaShieldAlt } from "react-icons/fa";

function Navbar() {
  return (
    <div className="navbar">
      <div className="navbar-left">
        <FaShieldAlt className="logo-icon" />
        <div>
          <h1>PromptShield</h1>
          <p>AI Firewall & Prompt Injection Detection Engine</p>
        </div>
      </div>
    </div>
  );
}

export default Navbar;