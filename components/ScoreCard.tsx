type Props = {
  result: {
    security_score: number;
    risk_level: string;
    issues_found: number;
  };
};

export default function ScoreCard({ result }: Props) {
  return (
    <div className="grid grid-cols-3 gap-4 mt-6">
      <div className="border rounded-lg p-4">
        <h3 className="text-sm text-gray-500">
          Security Score
        </h3>
        <p className="text-3xl font-bold">
          {result.security_score}
        </p>
      </div>

      <div className="border rounded-lg p-4">
        <h3 className="text-sm text-gray-500">
          Risk Level
        </h3>
        <p className="text-3xl font-bold">
          {result.risk_level}
        </p>
      </div>

      <div className="border rounded-lg p-4">
        <h3 className="text-sm text-gray-500">
          Issues Found
        </h3>
        <p className="text-3xl font-bold">
          {result.issues_found}
        </p>
      </div>
    </div>
  );
}