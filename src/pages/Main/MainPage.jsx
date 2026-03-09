// src/pages/Main/MainPage.jsx

import "./main.css";
import { inviteConfig } from "../../data/inviteConfig";

export default function MainPage() {
  const { couple, event, hero, inviteText } = inviteConfig;

  return (
    <main className="mainShell">
      <div className="mainContainer">
        {/* 1) HERO */}
        <section className="section heroSection">
          {hero.posterImage ? (
            <div
              className="heroImage"
              style={{ backgroundImage: `url(${hero.posterImage})` }}
              aria-hidden="true"
            />
          ) : (
            <div className="heroImageDummy" aria-hidden="true" />
          )}

          <div className="heroText">
            <p className="heroTagline">{hero.tagline}</p>

            <p className="heroTop">
              {couple.groom} ❤ {couple.bride}
            </p>

            <h1 className="heroTitle">{hero.title}</h1>

            <p className="heroMeta">
              {event.date} | {event.day} | {event.time}
              <br />
              {event.location}
            </p>
          </div>
        </section>

        {/* 2) INVITATION */}
        <section className="section inviteSection">
          <h2 className="sectionTitle">INVITATION</h2>
          <div className="inviteTextBox">
            {inviteText.map((line, idx) => (
              <p key={idx}>{line}</p>
            ))}
          </div>
        </section>

        {/* 3) FAMILY */}
        <section className="section familySection">
          <h2 className="sectionTitle">FAMILY</h2>
          <div className="familyGrid">
            <div>신랑측 가족 소개 (더미)</div>
            <div>신부측 가족 소개 (더미)</div>
          </div>
        </section>

        {/* 4) EVENT INFO */}
        <section className="section infoSection">
          <h2 className="sectionTitle">EVENT INFO</h2>
          <div className="infoBox">
            <p>D-DAY 영역 (추후 계산)</p>
            <p>지도 영역 (추후 카카오맵)</p>
            <p>계좌번호 영역</p>
          </div>
        </section>

        {/* 5) GALLERY */}
        <section className="section gallerySection">
          <h2 className="sectionTitle">GALLERY</h2>
          <div className="galleryGrid">
            <div className="galleryDummy" />
            <div className="galleryDummy" />
            <div className="galleryDummy" />
          </div>
        </section>

        {/* 6) GUESTBOOK */}
        <section className="section guestbookSection">
          <h2 className="sectionTitle">GUESTBOOK</h2>
          <div className="guestbookBox">방명록 영역 (추후 폼 추가)</div>
        </section>
      </div>
    </main>
  );
}
