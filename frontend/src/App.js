import React from "react";
import HeroSection from "./components/HeroSection";
import InvestorSection from "./components/InvestorSection";
import BuyerSection from "./components/BuyerSection"; 
import ProfessionalSection from "./components/REProSection";

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      {/* Hero section */}
      <HeroSection />

      {/* User Story Highlights */}
      <div className="container mx-auto py-8">
        <div className="text-center mb-8  space-y-2">
          <h2 className="text-3xl font-semibold text-gray-800">How Zulu Real Estate Can Help You</h2>
          <p className="text-right">
          Discover how <strong>Zulu</strong> meets the unique needs of investors, home buyers, and real estate professionals. Whether you're looking to make savvy investments with predictive analytics, find the perfect neighborhood with detailed comparisons, or provide accurate advice with in-depth market reports, our platform is designed to empower you with smart tools and insights for success in real estate.
          </p>
          <p className="text-gray-600 py-4">Choose a section below to learn more</p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <InvestorSection />
          <BuyerSection />
          <ProfessionalSection />
        </div>
      </div>

      {/* Footer and other sections */}
    </div>
  );
};
export default App;