#
# PySNMP MIB module CISCO-LLDP-EXT-MED-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LLDP-EXT-MED-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLldpExtMedCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 584))
ciscoLldpExtMedCapability.setRevisions(('2009-12-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setLastUpdated('200912020000Z')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLldpExtMedCapability.setDescription("This is the Agent Capabilities definition for\n        LLDP-EXT-MED-MIB'")
lldpExtMedCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 584, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setProductRelease('Cisco IOS 12.2SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpExtMedCapability1 = lldpExtMedCapability1.setStatus('current')
if mibBuilder.loadTexts: lldpExtMedCapability1.setDescription('LLDP MED MIB Capabilities')
mibBuilder.exportSymbols("CISCO-LLDP-EXT-MED-CAPABILITY", ciscoLldpExtMedCapability=ciscoLldpExtMedCapability, lldpExtMedCapability1=lldpExtMedCapability1, PYSNMP_MODULE_ID=ciscoLldpExtMedCapability)
