from pathlib import Path

# ===== 설정 =====
PROJECT_ROOT = Path.cwd()          # 실행 위치(프로젝트 루트) 기준
SRC = PROJECT_ROOT / "src"

# src 아래에 만들 구조
DIRS = [
    "app",
    "pages/Intro",
    "pages/Main",
    "sections/HeroPoster",
    "sections/Invitation",
    "sections/Family",
    "sections/WeddingInfo",
    "sections/Gallery",
    "sections/Guestbook",
    "sections/Extras",
    "components/Layout",
    "components/UI",
    "components/Effects",
    "components/Media",
    "data",
    "hooks",
    "utils",
    "styles",
    "services",
    "libs",
]

# src 아래에 만들 기본 파일(필요한 최소 템플릿 포함)
FILES = {
    "app/App.jsx": """import { Routes, Route, Navigate } from "react-router-dom";
import IntroPage from "../pages/Intro/IntroPage.jsx";
import MainPage from "../pages/Main/MainPage.jsx";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<IntroPage />} />
      <Route path="/main" element={<MainPage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
""",
    "pages/Intro/IntroPage.jsx": """import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import Typewriter from "../../components/Effects/Typewriter.jsx";
import FilmGrain from "../../components/Effects/FilmGrain.jsx";

export default function IntroPage() {
  const nav = useNavigate();
  const [ready, setReady] = useState(false);

  const lines = useMemo(
    () => [
      { text: "A WEDDING FILM", speed: 38, pause: 500 },
      { text: "DIRECTED BY LOVE", speed: 34, pause: 650 },
      { text: "COMING SOON", speed: 42, pause: 650 },
      { text: "PRESS ENTER TO BEGIN", speed: 26, pause: 0 },
    ],
    []
  );

  useEffect(() => {
    const onKeyDown = (e) => {
      if (e.key === "Enter") nav("/main");
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [nav]);

  return (
    <main className="introRoot">
      <FilmGrain />

      <div className="introPoster" aria-hidden="true">
        <div className="posterFrame" />
        <div className="posterGlow" />
      </div>

      <section className="introContent">
        <div className="badge">NOIR EDITION</div>

        <h1 className="introTitle">
          <span className="introTitleTop">THE</span>
          <span className="introTitleMain">INVITATION</span>
          <span className="introTitleBottom">TRAILER</span>
        </h1>

        <div className="typeArea">
          <Typewriter lines={lines} onDone={() => setReady(true)} />
        </div>

        <button
          className={`enterBtn ${ready ? "isReady" : ""}`}
          onClick={() => nav("/main")}
          disabled={!ready}
        >
          ENTER <span className="enterHint">/ MAIN</span>
        </button>

        <div className="credits">
          <span className="muted">© Once Studio / ONCE & ONLY</span>
        </div>
      </section>
    </main>
  );
}
""",
    "pages/Main/MainPage.jsx": """export default function MainPage() {
  return (
    <main className="appShell">
      <div className="card">
        <h1 className="title">MAIN PAGE</h1>
        <p className="muted">여기부터 섹션(포스터/초대글/갤러리/방명록) 붙일 예정</p>
      </div>
    </main>
  );
}
""",
    "components/Effects/Typewriter.jsx": """import { useEffect, useMemo, useState } from "react";

export default function Typewriter({ lines, onDone }) {
  const [lineIdx, setLineIdx] = useState(0);
  const [charIdx, setCharIdx] = useState(0);
  const [done, setDone] = useState(false);

  const current = useMemo(() => lines?.[lineIdx] ?? null, [lines, lineIdx]);

  useEffect(() => {
    if (!current || done) return;
    const speed = Math.max(12, current.speed ?? 30);

    const t = setTimeout(() => setCharIdx((c) => c + 1), speed);
    return () => clearTimeout(t);
  }, [current, charIdx, done]);

  useEffect(() => {
    if (!current || done) return;

    if (charIdx > current.text.length) {
      const pause = Math.max(0, current.pause ?? 300);
      const t = setTimeout(() => {
        if (lineIdx >= lines.length - 1) {
          setDone(true);
          onDone?.();
          return;
        }
        setLineIdx((i) => i + 1);
        setCharIdx(0);
      }, pause);

      return () => clearTimeout(t);
    }
  }, [charIdx, current, done, lineIdx, lines.length, onDone]);

  return (
    <div className="typeBox" role="status" aria-live="polite">
      {lines.map((l, i) => {
        const isActive = i === lineIdx && !done;
        const isPast = i < lineIdx || done;

        let text = "";
        if (isPast) text = l.text;
        else if (isActive) text = l.text.slice(0, Math.min(charIdx, l.text.length));

        return (
          <div className="typeLine" key={`${i}-${l.text}`}>
            <span className="typePrompt">{">"}</span>
            <span className="typeText">{text}</span>
            {isActive && <span className="cursor" aria-hidden="true" />}
          </div>
        );
      })}
    </div>
  );
}
""",
    "components/Effects/FilmGrain.jsx": """export default function FilmGrain() {
  return (
    <>
      <div className="vignette" aria-hidden="true" />
      <div className="grain" aria-hidden="true" />
      <div className="scanlines" aria-hidden="true" />
    </>
  );
}
""",
    "styles/globals.css": """*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; height:100%; }
body{
  background: var(--bg, #09090b);
  color: rgba(255,255,255,.92);
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Apple SD Gothic Neo, "Noto Sans KR", sans-serif;
  letter-spacing: .2px;
}
a{ color:inherit; text-decoration:none; }
button{ font: inherit; }
""",
    "styles/tokens.css": """:root{
  --bg: #09090b;
  --panel: rgba(255,255,255,.06);
  --stroke: rgba(255,255,255,.14);
  --text: rgba(255,255,255,.92);
  --muted: rgba(255,255,255,.68);
  --muted2: rgba(255,255,255,.52);
  --radius: 18px;
  --shadow: 0 18px 40px rgba(0,0,0,.55);
}
""",
    "styles/noir.css": """.appShell{
  max-width: 420px;
  margin: 0 auto;
  min-height: 100vh;
  padding: 18px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.card{
  width:100%;
  padding: 18px;
  border-radius: var(--radius);
  background: var(--panel);
  border: 1px solid var(--stroke);
  box-shadow: var(--shadow);
}
.title{ margin:0 0 8px; font-size: 22px; letter-spacing: 1px; }
.muted{ color: var(--muted); margin:0; }

/* Intro */
.introRoot{
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  display:flex;
  align-items:center;
  justify-content:center;
  padding: 22px 16px;
}
.introPoster{
  position:absolute;
  inset:-30px;
  background:
    radial-gradient(1200px 500px at 50% 30%, rgba(255,255,255,.10), transparent 60%),
    linear-gradient(0deg, rgba(0,0,0,.7), rgba(0,0,0,.88));
  filter: contrast(1.05) saturate(.8);
}
.posterFrame{
  position:absolute;
  left: 50%;
  top: 50%;
  width: min(420px, 88vw);
  height: min(620px, 78vh);
  transform: translate(-50%,-50%);
  border-radius: 26px;
  border: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.03);
  box-shadow: 0 30px 80px rgba(0,0,0,.65);
}
.posterGlow{
  position:absolute;
  left: 50%;
  top: 50%;
  width: min(520px, 100vw);
  height: min(720px, 90vh);
  transform: translate(-50%,-50%);
  border-radius: 40px;
  background: radial-gradient(closest-side, rgba(255,255,255,.09), transparent 68%);
  pointer-events:none;
}
.introContent{
  position: relative;
  z-index: 2;
  width: min(420px, 92vw);
  padding: 18px 16px;
  border-radius: var(--radius);
  background: rgba(0,0,0,.45);
  border: 1px solid rgba(255,255,255,.12);
  box-shadow: var(--shadow);
  backdrop-filter: blur(10px);
}
.badge{
  display:inline-flex;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(255,255,255,.06);
  color: var(--muted);
  font-size: 12px;
  letter-spacing: 1.4px;
}
.introTitle{ margin: 14px 0 14px; line-height: 1.0; text-transform: uppercase; }
.introTitleTop{ display:block; font-size: 12px; color: var(--muted2); letter-spacing: 3px; }
.introTitleMain{ display:block; font-size: 34px; letter-spacing: 4px; margin-top: 6px; }
.introTitleBottom{ display:block; font-size: 12px; color: var(--muted2); letter-spacing: 3px; margin-top: 6px; }

.typeBox{
  padding: 12px 12px;
  border-radius: 14px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.10);
}
.typeLine{
  display:flex;
  gap: 8px;
  align-items: baseline;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 13px;
  color: rgba(255,255,255,.82);
  padding: 4px 0;
}
.typePrompt{ color: rgba(255,255,255,.55); }
.cursor{
  width: 8px;
  height: 14px;
  margin-left: 2px;
  background: rgba(255,255,255,.55);
  display:inline-block;
  animation: blink 1s steps(1) infinite;
}
@keyframes blink{ 50%{ opacity: 0; } }

.enterBtn{
  margin-top: 14px;
  width: 100%;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.55);
  letter-spacing: 3px;
  text-transform: uppercase;
  cursor: not-allowed;
}
.enterBtn.isReady{
  cursor: pointer;
  color: rgba(255,255,255,.92);
  background: rgba(255,255,255,.10);
}
.enterHint{
  margin-left: 10px;
  letter-spacing: 1px;
  color: rgba(255,255,255,.55);
}

/* Film look */
.vignette{
  position:absolute;
  inset:-20px;
  background: radial-gradient(closest-side, transparent 55%, rgba(0,0,0,.75) 100%);
  z-index: 1;
  pointer-events:none;
}
.grain{
  position:absolute;
  inset:-40px;
  z-index: 3;
  pointer-events:none;
  opacity: .16;
  background-image:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)' opacity='.35'/%3E%3C/svg%3E");
  mix-blend-mode: overlay;
  animation: grainMove 6s steps(10) infinite;
}
@keyframes grainMove{
  0%{ transform: translate(0,0); }
  20%{ transform: translate(-3%,2%); }
  40%{ transform: translate(2%,-2%); }
  60%{ transform: translate(-2%,-3%); }
  80%{ transform: translate(3%,1%); }
  100%{ transform: translate(0,0); }
}
.scanlines{
  position:absolute;
  inset:-20px;
  z-index: 4;
  pointer-events:none;
  opacity: .08;
  background: repeating-linear-gradient(
    to bottom,
    rgba(255,255,255,.10) 0px,
    rgba(255,255,255,.10) 1px,
    transparent 2px,
    transparent 6px
  );
  mix-blend-mode: overlay;
}
""",
}

# ===== 실행 함수 =====
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str):
    if path.exists():
        # 이미 있으면 덮어쓰지 않게(원하면 True로 바꿔도 됨)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    if not SRC.exists():
        print(f"[오류] {SRC} 폴더가 없습니다. 프로젝트 루트에서 실행했는지 확인하세요.")
        return

    # 폴더 생성
    for d in DIRS:
        ensure_dir(SRC / d)

    # 기본 파일 생성
    for rel, content in FILES.items():
        write_file(SRC / rel, content)

    print("✅ src 폴더 구조 생성 완료!")
    print("다음 체크:")
    print("- src/app/App.jsx 생성됨")
    print("- src/pages/Intro/IntroPage.jsx 생성됨")
    print("- src/pages/Main/MainPage.jsx 생성됨")
    print("- src/styles/*.css 생성됨")

if __name__ == "__main__":
    main()
