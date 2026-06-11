"use client";

import { useState } from "react";
import Link from "next/link";

import UploadForm from "@/components/UploadForm";
import ScoreCard from "@/components/ScoreCard";
import FindingsTable from "@/components/FindingsTable";
import DownloadReport from "@/components/DownloadReport";

export default function Home() {
  const [result, setResult] = useState<any>(null);

  return (
    <main className="p-10">
      <div className="flex items-center justify-between mb-8">
        <h1 className="text-5xl font-bold">
          Smart Contract Auditor
        </h1>

        <Link
          href="/history"
          className="border px-4 py-2 rounded"
        >
          View Scan History
        </Link>
      </div>

      <UploadForm onResult={setResult} />

      {result && (
        <>
          <ScoreCard result={result} />

          <FindingsTable
            findings={result.findings}
          />

          <div className="mt-8">
            <h2 className="text-2xl font-bold">
              AI Explanation
            </h2>

            <p className="mt-2 whitespace-pre-line">
              {result.explanation}
            </p>
          </div>

          <div className="mt-8">
            <h2 className="text-2xl font-bold">
              Remediation
            </h2>

            <p className="mt-2">
              {result.remediation}
            </p>
          </div>

          <DownloadReport />
        </>
      )}
    </main>
  );
}