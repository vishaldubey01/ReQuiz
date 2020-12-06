import Head from "next/head";
import Features from "../components/Features";
import Footer from "../components/footer";
import Hero from "../components/Hero";
import Navbar from "../components/Navbar";
var data = require("../data/questions.json");

export default function Home() {
  console.log(data);
  return (
    <div>
      <Head>
        <title>ReQuiz</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar logo />
      <main>
        <Hero />
        <br></br>
        <br></br>
        <br></br>
        <Features />
      </main>
      <br></br>
      <br></br>
      <br></br>
      <Footer />
    </div>
  );
}
