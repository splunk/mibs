#
# PySNMP MIB module CISCO-EVC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-EVC-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoEvcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 568))
ciscoEvcCapability.setRevisions(('2008-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEvcCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEvcCapability.setLastUpdated('200808260000Z')
if mibBuilder.loadTexts: ciscoEvcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEvcCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n            USA\n            Tel: +1 800 553-NETS\n            E-mail:  cs-ethermibs@cisco.com')
if mibBuilder.loadTexts: ciscoEvcCapability.setDescription('Agent capabilities for the CISCO-EVC-MIB.')
ciscoEvcCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2 SR Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setStatus('current')
if mibBuilder.loadTexts: ciscoEvcCapabilityV12R02SR.setDescription('CISCO-EVC-MIB capabilities.')
ciscoEvcCapabilityV12R02XO = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setProductRelease('Cisco IOS 12.2 XO Release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setStatus('current')
if mibBuilder.loadTexts: ciscoEvcCapabilityV12R02XO.setDescription('CISCO-EVC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-EVC-CAPABILITY", ciscoEvcCapabilityV12R02XO=ciscoEvcCapabilityV12R02XO, ciscoEvcCapability=ciscoEvcCapability, PYSNMP_MODULE_ID=ciscoEvcCapability, ciscoEvcCapabilityV12R02SR=ciscoEvcCapabilityV12R02SR)
