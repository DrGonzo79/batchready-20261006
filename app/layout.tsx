import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"BatchReady — Retail readiness workspace",description:"Turn SKU evidence into a founder-reviewed retail readiness packet."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
