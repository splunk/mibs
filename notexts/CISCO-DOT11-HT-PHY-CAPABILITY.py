#
# PySNMP MIB module CISCO-DOT11-HT-PHY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-HT-PHY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cDot11HtPhyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 551))
cDot11HtPhyCapability.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: cDot11HtPhyCapability.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setOrganization('Cisco Systems, Inc.')
cDot11HtPhyCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 551, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-HT-PHY-CAPABILITY", PYSNMP_MODULE_ID=cDot11HtPhyCapability, cDot11HtPhyCapability=cDot11HtPhyCapability, cDot11HtPhyCapabilityV12R0410BJA=cDot11HtPhyCapabilityV12R0410BJA)
