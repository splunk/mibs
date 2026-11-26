#
# PySNMP MIB module LANOPTICS-BRIDGE-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, enterprises, ModuleIdentity, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "enterprises", "ModuleIdentity", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsBridgeProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6))
lanOpticsLMGRAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6, 8))
lanOpticsLMGRLinkID = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setStatus('mandatory')
lanOpticsLMGRCaptCntrlLink = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-BRIDGE-OPTION-MIB", lanOpticsBridgeProxyAgent=lanOpticsBridgeProxyAgent, lanOpticsLMGRLinkID=lanOpticsLMGRLinkID, lanOptics=lanOptics, lanOpticsLMGRCaptCntrlLink=lanOpticsLMGRCaptCntrlLink, lanOpticsLMGRAgent=lanOpticsLMGRAgent)
