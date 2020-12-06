import Head from "next/head";
import Footer from "../components/footer";
import Hero from "../components/Hero";
import Navbar from "../components/Navbar";

export default function Home() {
  return (
    <div>
      <Head>
        <title>ReQuiz</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar logo />
      <main>
        <Hero />
      </main>
      <Footer />
    </div>
  );
}
