type Finding = {
  check: string;
  severity: string;
  description: string;
};

export default function FindingsTable({
  findings,
}: {
  findings: Finding[];
}) {
  const getSeverityClass = (severity: string) => {
    switch (severity?.toLowerCase()) {
      case "high":
        return "bg-red-500 text-white";
      case "medium":
        return "bg-yellow-500 text-white";
      case "low":
        return "bg-blue-500 text-white";
      default:
        return "bg-gray-300 text-black";
    }
  };

  return (
    <div className="mt-8">
      <h2 className="text-2xl font-bold mb-4">
        Findings
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full border border-gray-300 rounded-lg">
          <thead>
            <tr className="bg-gray-100 border-b">
              <th className="text-left p-3">
                Check
              </th>

              <th className="text-left p-3">
                Severity
              </th>

              <th className="text-left p-3">
                Description
              </th>
            </tr>
          </thead>

          <tbody>
            {findings.map((finding, index) => (
              <tr
                key={index}
                className="border-b hover:bg-gray-50"
              >
                <td className="p-3 font-medium">
                  {finding.check}
                </td>

                <td className="p-3">
                  <span
                    className={`px-3 py-1 rounded-full text-sm font-semibold ${getSeverityClass(
                      finding.severity
                    )}`}
                  >
                    {finding.severity}
                  </span>
                </td>

                <td className="p-3 whitespace-pre-wrap text-sm">
                  {finding.description}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}