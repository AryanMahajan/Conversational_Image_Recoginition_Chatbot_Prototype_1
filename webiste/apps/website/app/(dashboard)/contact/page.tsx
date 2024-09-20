import { ContactDetails } from "../../../components/ContactDetails";
import { TopBar } from "../../../components/TopBar";





export default function Page() {
    return <div className="min-h-screen bg-zinc-800">
        <TopBar />
        <div className="h-screen">
        <ContactDetails />

        </div>
    </div>
}
