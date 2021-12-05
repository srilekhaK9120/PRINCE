import Head from "next/head";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Sendbox from "./components/Sendbox";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 max-h-screen bg-gray-900">
      <Head>
        <title>Encryption/Decryption using PrinceCipher</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className="flex justify-around text-gray-300">
        <Sendbox
          m1="Encryption"
          m2="encrypt"
          m3="Enter the text to encrypt..."
          m4="enc"
          m5="encrypted_message"
        />
        <Sendbox
          m1="Decryption"
          m2="decrypt"
          m3="Enter the text to decrypt..."
          m4="dec"
          m5="decrypted_message"
        />
      </div>
      <Footer />
    </div>
  );
}
