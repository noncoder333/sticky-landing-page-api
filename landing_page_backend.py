import React, { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("http://localhost:5000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      if (response.ok) {
        setResult(data);
      } else {
        setError(data.error || "Something went wrong");
      }
    } catch (err) {
      setError("Failed to connect to server");
    }
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "20px" }}>
      <h2>Landing Page Extractor</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter landing page URL"
          style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Submit"}
        </button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Results:</h3>
          <p><strong>Product ID:</strong> {result.sticky_io?.product_id}</p>
          <p><strong>Campaign ID:</strong> {result.sticky_io?.campaign_id}</p>
          <p><strong>HTML Extracted:</strong></p>
          <textarea value={result.html} readOnly rows={10} style={{ width: "100%" }}></textarea>
          <p><strong>CSS Extracted:</strong></p>
          <textarea value={result.css} readOnly rows={5} style={{ width: "100%" }}></textarea>
        </div>
      )}
    </div>
  );
}

export default App;
