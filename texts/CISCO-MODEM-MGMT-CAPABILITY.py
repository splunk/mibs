#
# PySNMP MIB module CISCO-MODEM-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODEM-MGMT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoModemMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoModemMgmtCapability.setRevisions(('2006-07-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModemMgmtCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setLastUpdated('200607310000Z')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setDescription('Agent capabilities for CISCO-MODEM-MGMT-MIB.')
ciscoModemMgmtCapV12R4TISR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setProductRelease('Cisco IOS 12.4 for ATG Platform Devices')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setStatus('current')
if mibBuilder.loadTexts: ciscoModemMgmtCapV12R4TISR.setDescription('CISCO-MODEM-MGMT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODEM-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoModemMgmtCapability, ciscoModemMgmtCapV12R4TISR=ciscoModemMgmtCapV12R4TISR, ciscoModemMgmtCapability=ciscoModemMgmtCapability)
