export default function DownloadReport() {
  return (
    <div className="mt-6">
      <a
        href="http://127.0.0.1:8000/download-report"
        target="_blank"
        className="border px-4 py-2 rounded"
      >
        Download PDF Report
      </a>
    </div>
  );
}