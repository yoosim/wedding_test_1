import { useEffect, useMemo, useState } from "react";

/*
  🎬 느와르 타자 버전

  - 글자 단위 타이핑
  - 공백/쉼표/마침표에서 약간 멈춤
  - 한 줄 끝나면 2초 멈춤 후 다음 줄
*/

export default function Typewriter({ lines = [], onDone }) {
  const [lineIdx, setLineIdx] = useState(0);   // 현재 줄
  const [charIdx, setCharIdx] = useState(0);   // 현재 글자
  const [done, setDone] = useState(false);     // 전체 완료 여부

  const current = useMemo(() => lines[lineIdx], [lines, lineIdx]);

  useEffect(() => {
    if (!current || done) return;

    const fullText = current.text;

    // 현재 줄이 완성되었는지 체크
    if (charIdx > fullText.length) {
      const timeout = setTimeout(() => {
        if (lineIdx >= lines.length - 1) {
          setDone(true);
          onDone?.();
        } else {
          setLineIdx((prev) => prev + 1);
          setCharIdx(0);
        }
      }, 2000); // ✅ 줄 끝 멈춤 (2초)

      return () => clearTimeout(timeout);
    }

    // 🔥 기본 속도 (또각또각 느낌)
    let delay = 130;

    // 🔥 리듬 조절
    const currentChar = fullText[charIdx - 1];

    if (currentChar === " ") delay = 40;            // 공백에서 살짝 멈춤
    if (currentChar === "," ) delay = 120;
    if (currentChar === "." ) delay = 150;
    if (currentChar === "!" ) delay = 160;
    if (currentChar === "?" ) delay = 160;

    const timeout = setTimeout(() => {
      setCharIdx((prev) => prev + 1);
    }, delay);

    return () => clearTimeout(timeout);

  }, [charIdx, current, done, lineIdx, lines.length, onDone]);

  return (
    <div className="typeBox">
      {lines.map((line, i) => {
        const isPast = i < lineIdx || done;
        const isActive = i === lineIdx && !done;

        let text = "";
        if (isPast) text = line.text;
        else if (isActive) text = line.text.slice(0, charIdx);

        return (
          <div className="typeLine" key={i}>
            <span className="typePrompt">{">"}</span>
            <span className="typeText">{text}</span>
            {isActive && <span className="cursor" />}
          </div>
        );
      })}
    </div>
  );
}
