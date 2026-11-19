#
# PySNMP MIB module CISCO-ITP-MSU-RATES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MSU-RATES-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
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
ciscoItpMsuRatesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 537))
ciscoItpMsuRatesCapability.setRevisions(('2007-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setLastUpdated('200703200000Z')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-itp@cisco.com')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setDescription('Agent capabilities for the CISCO-ITP-MSU-RATES-MIB.')
ciscoItpMsuCapabilityV12R0225SW7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setProductRelease('Cisco IOS 12.2(25)SW7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0225SW7.setDescription('Cisco IOS 12.2(25)SW7 CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0218IXB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setProductRelease('Cisco IOS 12.2(18)IXB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0218IXB.setDescription('Cisco IOS 12.2(18)IXB CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MSU-RATES-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0411SW=ciscoItpMsuCapabilityV12R0411SW, ciscoItpMsuCapabilityV12R0225SW7=ciscoItpMsuCapabilityV12R0225SW7, ciscoItpMsuRatesCapability=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0218IXB=ciscoItpMsuCapabilityV12R0218IXB)
