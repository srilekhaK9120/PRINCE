import Head from "next/head";
import Link from "next/link";
import Footer from "./components/Footer";
import Header from "./components/Header";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-gray-900">
      <Head>
        <title>Cryptography_CS553</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center text-gray-300 mt-5">
        <h1 className="text-6xl font-bold">
          Prince Encrypter and Decrypter (E&D) Solutions
        </h1>
        <p className="mt-3 text-2xl font-bold">
          Team ILLUMINATI @PrinceCipher{" "}
          <code className="p-1 ml-1 font-mono text-lg bg-gray-600 rounded-md">
            <a href="https://github.com/srilekhaK9120/PRINCE.git">github link</a>
          </code>
        </p>

        <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
          <a
            href="/enc_dec"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">Encryption/Decyrption &rarr;</h3>
            <p className="mt-4 text-xl">
              Encrypt/Decrypt any text using prince cipher.
            </p>
          </a>

          <a
            href="/learn"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">Learn &rarr;</h3>
            <p className="mt-4 text-xl">
              Prince Cipher resources and our course details.
            </p>
          </a>

          <a
            href="/chat"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">Chat Application &rarr;</h3>
            <p className="mt-4 text-xl">
              Socket programed, secure(prince at the ground) Group Chat
              Application.
            </p>
          </a>

          <a
            href="/aboutCourse"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-green-600 focus:text-green-600 hover:font-bold"
          >
            <h3 className="text-2xl font-bold">About Course &rarr;</h3>
            <p className="mt-4 text-xl">
              Name: CS553_2021, Cryptography Instructor: Dhiman Saha
            </p>
          </a>

          <a
            href="/"
            className="p-6 mt-6 text-left border w-192 rounded-xl  focus:text-green-600"
          >
            <h3 className="text-2xl font-bold hover:text-green-600">
              Team Members @ IITBhilai &rarr;
            </h3>
            <p className="mt-4 text-xl">
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                <a href="/">yaadava_kishore(11940310)</a>
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                <a href="/">vivek_mulukula(11940720)</a>
              </code>
              <code className="p-2 m-2 font-semibold font-mono text-lg bg-gray-600 rounded-md hover:text-blue-400">
                <a href="/">srilekha_kadambala(11941190)</a>
              </code>
            </p>
          </a>
        </div>
      </main>
      <Footer />
    </div>
  );
}
