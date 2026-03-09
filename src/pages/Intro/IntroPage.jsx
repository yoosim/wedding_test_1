import { useCallback, useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import Typewriter from "../../components/Effects/Typewriter.jsx";
import FilmGrain from "../../components/Effects/FilmGrain.jsx";

export default function IntroPage() {
  const nav = useNavigate();

  // ready: 타이핑 완료 후 ENTER 버튼 활성화
  const [ready, setReady] = useState(false);

  // cutting: 필름컷 전환 중(중복 클릭 방지)
  const [cutting, setCutting] = useState(false);

  // 타이핑 문구(원하는대로 바꾸면 됨)
  const lines = useMemo(
    () => [
      { text: "안녕하세요 여러분 김재현,신아영 입니다" },
      { text: "2026년 5월 16일 오전 11시 결혼합니다." },
      { text: "저희둘의 새로운 시작을 축하해주세요." },
      { text: "결혼식에 초대합니다." },
    ],
    []
  );

  // 메인으로 이동(필름컷 애니메이션 후 이동)
  // const goMain = useCallback(() => {
  //   if (!ready || cutting) return;
  //   setCutting(true);
  //   setTimeout(() => nav("/main"), 650);
  // }, [ready, cutting, nav]);
  // 테스트용
  const goMain = useCallback(() => {
    console.log("goMain called", { ready, cutting });
    if (!ready || cutting) return;

    setCutting(true);
    console.log("cutting set true, will navigate in 650ms");

    setTimeout(() => {
      console.log("timeout fired -> navigate /main");
      nav("/main");
    }, 650);
  }, [ready, cutting, nav]);

  // Enter 키로도 이동
  useEffect(() => {
    const onKeyDown = (e) => {
      if (e.key === "Enter") goMain();
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [goMain]); // ready/cutting 바뀌면 최신 goMain 조건 반영

  return (
    <main className={`introRoot ${cutting ? "isCutting" : ""}`}>
      {/* ✅ 모바일 화면처럼 보이도록 중앙 고정 프레임 */}
      <div className="mobileFrame">
        {/* ✅ 필름 느낌(비네트/노이즈/스캔라인) */}
        <FilmGrain />

        {/* ✅ 배경 이미지: 프레임 안에서만 보임 */}
        <div className="introPoster" aria-hidden="true" />

        {/* ✅ ENTER 눌렀을 때 필름컷(깜빡/컷) 오버레이 */}
        <div className="filmCut" aria-hidden="true" />

        {/* ✅ 콘텐츠 카드 */}
        <section className="introContent">
          <div className="badge">IN ASSOCIATION WITH LOVE</div>

          <h1 className="introTitle">
            <span className="introTitleTop">김재현 ❤ 신아영 결혼합니다</span>
            <span className="introTitleMain"> OUR WEDDING</span>
            <span className="introTitleBottom">2026.05.16 | SAT | 11:00 | 서울 신라호텔</span>
          </h1>

          <div className="typeArea">
            <Typewriter lines={lines} onDone={() => setReady(true)} />
          </div>

          <button
            className={`enterBtn ${ready ? "isReady" : ""}`}
            onClick={goMain}
            disabled={!ready || cutting}
          >
            ENTER <span className="enterHint">/ MAIN</span>
          </button>

          <div className="credits">
            <span className="muted">© Once Studio / small</span>
          </div>
        </section>
      </div>
    </main>
  );
}
