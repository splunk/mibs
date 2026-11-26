#
# PySNMP MIB module CISCO-DOT11-HT-PHY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-HT-PHY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
cDot11HtPhyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 551))
cDot11HtPhyCapability.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDot11HtPhyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cDot11HtPhyCapability.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setDescription('Agent capabilities for CISCO-DOT11-HT-PHY-MIB')
cDot11HtPhyCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 551, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setStatus('current')
if mibBuilder.loadTexts: cDot11HtPhyCapabilityV12R0410BJA.setDescription('CISCO-DOT11-HT-PHY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-HT-PHY-CAPABILITY", cDot11HtPhyCapabilityV12R0410BJA=cDot11HtPhyCapabilityV12R0410BJA, PYSNMP_MODULE_ID=cDot11HtPhyCapability, cDot11HtPhyCapability=cDot11HtPhyCapability)
