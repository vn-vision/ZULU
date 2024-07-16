import React from 'react';
import pros from '../assets/images/pros.jpg';

const ProfessionalSection = () => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="p-4">
        <h2 className="text-xl font-semibold text-gray-800 mb-2">Empower Your Clients</h2>
        <p className="text-gray-600 mb-4">
          Generate detailed market analysis reports to provide accurate advice to your clients.
        </p>
        <div className="border border-gray-200 rounded-lg overflow-hidden">
         
          {/* Replace with your actual report generation tool screenshot */}
          <img src={pros} alt="Report Generation Tool" className="w-full" />
        </div>
        <div className="mt-4">
          <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md shadow-md focus:outline-none">
            Generate Reports
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProfessionalSection;
