// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BiometricRegistry {
    struct IdentityClaim {
        string socialUrl;
        bytes32 faceVectorHash;
        uint256 timestamp;
        bool isVerified;
    }

    // Mapping a user's wallet address to their biometric identity claim
    mapping(address => IdentityClaim) public verifiedIdentities;

    event IdentityRegistered(address indexed user, string socialUrl, uint256 timestamp);

    /**
     * @dev Registers a verified biometric claim to the blockchain.
     * In a production app, this would use EIP-712 signatures to prevent spoofing.
     */
    function registerIdentity(string memory _socialUrl, bytes32 _faceVectorHash) public {
        require(!verifiedIdentities[msg.sender].isVerified, "Identity already registered");

        verifiedIdentities[msg.sender] = IdentityClaim({
            socialUrl: _socialUrl,
            faceVectorHash: _faceVectorHash,
            timestamp: block.timestamp,
            isVerified: true
        });

        emit IdentityRegistered(msg.sender, _socialUrl, block.timestamp);
    }

    /**
     * @dev Allows third-party dApps to verify if a user is a unique human.
     */
    function getIdentity(address _user) public view returns (string memory, bytes32, uint256, bool) {
        IdentityClaim memory claim = verifiedIdentities[_user];
        return (claim.socialUrl, claim.faceVectorHash, claim.timestamp, claim.isVerified);
    }
}