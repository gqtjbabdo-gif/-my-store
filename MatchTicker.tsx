import { useEffect, useState } from 'react';

const MatchTicker = () => {
  const [matches, setMatches] = useState<any[]>([]);

  useEffect(() => {
    fetch('/matches.json')
      .then(res => res.json())
      .then(data => setMatches(data))
      .catch(err => console.error("خطأ في جلب النتائج:", err));
  }, []);

  return (
    <div className="match-container" style={{ padding: '20px', background: '#f9f9f9', borderRadius: '8px', margin: '10px 0' }}>
      <h2 style={{ textAlign: 'center' }}>نتائج المباريات الحية</h2>
      {matches.length > 0 ? matches.map((match: any, index: number) => (
        <div key={index} style={{ borderBottom: '1px solid #ddd', padding: '10px' }}>
          <strong>{match.home} vs {match.away}</strong> - النتيجة: {match.score}
        </div>
      )) : <p style={{ textAlign: 'center' }}>جاري تحديث النتائج...</p>}
    </div>
  );
};

export default MatchTicker;
