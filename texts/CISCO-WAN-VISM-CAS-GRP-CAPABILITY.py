#
# PySNMP MIB module CISCO-WAN-VISM-CAS-GRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-CAS-GRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismCasGrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 333))
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setLastUpdated('200012050000Z')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setDescription('The Agent Capabilities for vismCasGrp.my .')
cwvismCasGrpCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setProductRelease('VISM Release 2.1.0 and MGX-8850 Release 1.1.34')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setStatus('current')
if mibBuilder.loadTexts: cwvismCasGrpCapability1.setDescription('vismCasGrp.my Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-CAS-GRP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismCasGrpCapability, ciscoWanVismCasGrpCapability=ciscoWanVismCasGrpCapability, cwvismCasGrpCapability1=cwvismCasGrpCapability1)
