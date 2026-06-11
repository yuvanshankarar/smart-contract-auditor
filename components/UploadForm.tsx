"use client";

import { useState } from "react";

export default function UploadForm({
  onResult,
}: {
  onResult: (data: any) => void;
}) {
  const [file, setFile] = useState<File | null>(null);

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(
      "http://127.0.0.1:8000/scan-contract",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await response.json();

    onResult(data);
  };

  return (
    <div className="space-y-4">
      <input
        type="file"
        accept=".sol"
        onChange={(e) =>
          setFile(e.target.files?.[0] || null)
        }
      />

      <button
        onClick={uploadFile}
        className="border px-4 py-2 rounded"
      >
        Scan Contract
      </button>
    </div>
  );
}