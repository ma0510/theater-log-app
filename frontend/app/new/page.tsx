"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const CATEGORIES = ["ミュージカル（劇団四季）", "ミュージカル（その他）", "歌舞伎", "その他"];
const SHOW_TIMES = ["マチネ", "ソワレ", "昼の部", "夜の部", "1部", "2部", "3部"];

type CastInput = {
  role_name: string;
  cast_name: string;
};

export default function NewPerformance() {
  const router = useRouter();

  const [category, setCategory] = useState(CATEGORIES[0]);
  const [title, setTitle] = useState("");
  const [watchedDate, setWatchedDate] = useState("");
  const [showTime, setShowTime] = useState(SHOW_TIMES[0]);
  const [seat, setSeat] = useState("");
  const [seatType, setSeatType] = useState("");
  const [memo, setMemo] = useState("");
  const [casts, setCasts] = useState<CastInput[]>([{ role_name: "", cast_name: "" }]);

  const addCastRow = () => {
    setCasts([...casts, { role_name: "", cast_name: "" }]);
  };

  const updateCast = (index: number, field: keyof CastInput, value: string) => {
    const newCasts = [...casts];
    newCasts[index][field] = value;
    setCasts(newCasts);
  };

  const removeCast = (index: number) => {
    setCasts(casts.filter((_, i) => i !== index));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const body = {
      category,
      title,
      watched_date: watchedDate,
      show_time: showTime,
      seat,
      seat_type: seatType,
      memo: memo || null,
      casts,
    };

    const res = await fetch("https://theater-log-app.onrender.com/performances", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (res.ok) {
      router.push("/");
    } else {
      alert("登録に失敗しました");
    }
  };

  return (
    <main style={{ padding: "20px", maxWidth: "500px" }}>
      <h1>観劇記録を登録</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
        <label>
          カテゴリ
          <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ width: "100%" }}>
            {CATEGORIES.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
        </label>

        <label>
          公演名
          <input value={title} onChange={(e) => setTitle(e.target.value)} required style={{ width: "100%" }} />
        </label>

        <label>
          日付
          <input type="date" value={watchedDate} onChange={(e) => setWatchedDate(e.target.value)} required style={{ width: "100%" }} />
        </label>

        <label>
          上演時間
          <select value={showTime} onChange={(e) => setShowTime(e.target.value)} style={{ width: "100%" }}>
            {SHOW_TIMES.map((s) => (
              <option key={s} value={s}>{s}</option>
            ))}
          </select>
        </label>

        <label>
          座席
          <input value={seat} onChange={(e) => setSeat(e.target.value)} style={{ width: "100%" }} />
        </label>

        <label>
          席種
          <input value={seatType} onChange={(e) => setSeatType(e.target.value)} style={{ width: "100%" }} />
        </label>

        <div>
          <p>キャスト</p>
          {casts.map((cast, i) => (
            <div key={i} style={{ display: "flex", gap: "8px", marginBottom: "8px" }}>
              <input
                placeholder="役名"
                value={cast.role_name}
                onChange={(e) => updateCast(i, "role_name", e.target.value)}
                style={{ flex: 1 }}
              />
              <input
                placeholder="キャスト名"
                value={cast.cast_name}
                onChange={(e) => updateCast(i, "cast_name", e.target.value)}
                style={{ flex: 1 }}
              />
              {casts.length > 1 && (
                <button type="button" onClick={() => removeCast(i)}>削除</button>
              )}
            </div>
          ))}
          <button type="button" onClick={addCastRow}>+ キャストを追加</button>
        </div>

        <label>
          感想
          <textarea value={memo} onChange={(e) => setMemo(e.target.value)} style={{ width: "100%" }} />
        </label>

        <button type="submit">登録する</button>
      </form>
    </main>
  );
}
