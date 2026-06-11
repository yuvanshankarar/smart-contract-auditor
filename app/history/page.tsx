"use client";

import { useEffect, useState } from "react";

export default function HistoryPage() {
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/history")
      .then((res) => res.json())
      .then(setHistory);
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-4xl font-bold mb-6">
        Scan History
      </h1>

      {history.map((scan, index) => (
        <div
          key={index}
          className="border rounded p-4 mb-4"
        >
          <p>
            <b>Contract:</b>{" "}
            {scan.filename}
          </p>

          <p>
            <b>Score:</b>{" "}
            {scan.score}
          </p>

          <p>
            <b>Risk:</b>{" "}
            {scan.risk_level}
          </p>
        </div>
      ))}
    </main>
  );
}