#
# PySNMP MIB module CISCO-CABLE-ADM-C-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CABLE-ADM-C-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableAdmCtrlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 427))
ciscoCableAdmCtrlCapability.setRevisions(('2004-12-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setRevisionsDescriptions(('This is the initial version.',))
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setLastUpdated('200412110000Z')
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setContactInfo('         Cisco Systems\n                      Customer Service\n\n            Postal:   Cisco Systems\n                      170 West Tasman Drive\n                      San Jose, CA 95134\n                      U.S.A.\n            Phone:    +1 800 553-NETS\n            E-mail:   cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapability.setDescription('Agent capabilities for CISCO-CABLE-ADMISSION-CTR-MIB')
ciscoCableAdmCtrlCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 427, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAdmCtrlCapabilityV12R00 = ciscoCableAdmCtrlCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableAdmCtrlCapabilityV12R00 = ciscoCableAdmCtrlCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableAdmCtrlCapabilityV12R00.setDescription('Cisco Cable Admission Control MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-ADM-C-CAPABILITY", ciscoCableAdmCtrlCapability=ciscoCableAdmCtrlCapability, PYSNMP_MODULE_ID=ciscoCableAdmCtrlCapability, ciscoCableAdmCtrlCapabilityV12R00=ciscoCableAdmCtrlCapabilityV12R00)
