const hre = require("hardhat");

async function main() {
  const OSINT = await hre.ethers.getContractFactory("BiometricOSINT");
  const osint = await OSINT.deploy();
  await osint.waitForDeployment();
  console.log(`BiometricOSINT deployed to: ${await osint.getAddress()}`);
}
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});