import { Routes, Route, Navigate } from "react-router-dom";
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
