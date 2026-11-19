#
# PySNMP MIB module CISCO-CABLE-WIDEBAND-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CABLE-WIDEBAND-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention")
ciscoCableWidebandCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 520))
ciscoCableWidebandCapability.setRevisions(('2010-06-09 00:00', '2006-09-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableWidebandCapability.setRevisionsDescriptions(('Add notInService status for ccwbRFChannelRowStatus', 'This is the Initial version',))
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setLastUpdated('201006090000Z')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: Cisco Systems\n            170 West Tasman Drive\n            San Jose, CA 95134\n            U.S.A.\n            Phone:  +1 800 553-NETS\n            E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setDescription('Agent capabilities for CISCO-CABLE-WIDEBAND-MIB')
ciscoCableWidebandCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV12R00.setDescription('Cisco Cable Wideband MIB capabilities.')
ciscoCableWidebandCapabilityV122R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV122R00.setDescription('Cisco Cable Wideband MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-WIDEBAND-CAPABILITY", ciscoCableWidebandCapabilityV122R00=ciscoCableWidebandCapabilityV122R00, PYSNMP_MODULE_ID=ciscoCableWidebandCapability, ciscoCableWidebandCapabilityV12R00=ciscoCableWidebandCapabilityV12R00, ciscoCableWidebandCapability=ciscoCableWidebandCapability)
