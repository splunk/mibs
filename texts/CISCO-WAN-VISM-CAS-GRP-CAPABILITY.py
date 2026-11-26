#
# PySNMP MIB module CISCO-WAN-VISM-CAS-GRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-CAS-GRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-WAN-VISM-CAS-GRP-CAPABILITY", cwvismCasGrpCapability1=cwvismCasGrpCapability1, PYSNMP_MODULE_ID=ciscoWanVismCasGrpCapability, ciscoWanVismCasGrpCapability=ciscoWanVismCasGrpCapability)
