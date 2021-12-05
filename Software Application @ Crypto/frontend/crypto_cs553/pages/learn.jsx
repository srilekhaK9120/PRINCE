import Head from "next/head";
import Link from "next/link";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Sendbox from "./components/Sendbox";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen py-2 justify-center items-center bg-gray-900">
      <Head>
        <title>Learn prince cipher</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className="fixed top-60 flex flex-col w-600">
        <div className="font-bold text-center text-green-300 text-3xl">
          Learning resources
        </div>
        <div className="mt-4 text-center">
          <code className="p-1 text-lg bg-gray-400 font-bold rounded-md">
            Wikipedia:
          </code>
          <span className="text-gray-300 text-lg font-bold p-1 ml-2 hover:text-blue-400">
            <Link href="https://en.wikipedia.org/wiki/Prince_(cipher)">
              Short introduction about prince cipher
            </Link>
          </span>   
        </div>
        <div className="mt-4 text-center">
          <code className="p-1 text-lg bg-gray-400 font-bold rounded-md">
            Official paper:
          </code>
          <span className="text-gray-300 text-lg font-bold p-1 ml-2 hover:text-blue-400">
            <Link href="https://eprint.iacr.org/2012/529.pdf">
              For overall understanding of prince cipher
            </Link>
          </span>   
        </div>
        <div className="mt-4 text-center">
          <code className="p-1 text-lg bg-gray-400 font-bold rounded-md">
            other resources:
          </code>
          <span className="text-gray-300 text-lg font-bold p-1 ml-2 hover:text-blue-400">
            <Link href="http://eprint.iacr.org/2012/712">
            Cryptology ePrint Archive: Report 2012/712
            </Link>
          </span>   
        </div>
        <div className="mt-4 text-center">
          <code className="p-1 text-lg bg-gray-400 font-bold rounded-md">
            other resources:
          </code>
          <span className="text-gray-300 text-lg font-bold p-1 ml-2 hover:text-blue-400">
            <Link href="https://onlinelibrary.wiley.com/doi/epdf/10.1002/sec.1213">
           Truncated differential cryptanalysis of prince
            </Link>
          </span>   
        </div>
      </div>

      <Footer />
    </div>
  );
}
