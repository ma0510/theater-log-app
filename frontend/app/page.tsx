"use client";

import { useEffect, useState } from "react";

type Cast = {
  id: number;
  role_name: string;
  cast_name: string;
};

type Performance = {
  id: number;
  category: string;
  title: string;
  watched_date: string;
  show_time: string;
  seat: string;
  seat_type: string;
  memo: string | null;
  casts: Cast[];
};

export default function Home() {
  const [performances, setPerformances] = useState<Performance[]>([]);

  useEffect(() => {
    fetch("https://organic-space-engine-69p59qxqrjxwf477w-8000.app.github.dev/performances")
      .then((res) => res.json())
      .then((data) => setPerformances(data));
  }, []);

  return (
    <main style={{ padding: "20px" }}>
      <h1>観劇記録一覧</h1>
      {performances.map((p) => (
        <div
          key={p.id}
          style={{ border: "1px solid #ccc", padding: "12px", marginBottom: "12px" }}
        >
          <p>{p.category}</p>
          <h2>{p.title}</h2>
          <p>{p.watched_date} / {p.show_time}</p>
          <p>座席: {p.seat}（{p.seat_type}）</p>
          <p>
            キャスト: {p.casts.map((c) => `${c.role_name}: ${c.cast_name}`).join(", ")}
          </p>
          {p.memo && <p>感想: {p.memo}</p>}
        </div>
      ))}
    </main>
  );
}