#
# PySNMP MIB module LANOPTICS-BRIDGE-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ModuleIdentity, MibIdentifier, enterprises, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ModuleIdentity", "MibIdentifier", "enterprises", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsBridgeProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6))
lanOpticsLMGRAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6, 8))
lanOpticsLMGRLinkID = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setDescription('When LMGR session is active with PCRouter card through PCBus -\n         this variable gives the LRM Session Link Number (0-3) between\n         the Host (SNMP agent) and the PCRouter LAN Reporting Mechanism.')
lanOpticsLMGRCaptCntrlLink = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setDescription("When LMGR session is active with PCRouter card through PCBus -\n         this variable is by default enabled (1). It means that the Host \n         (SNMP Agent) tries to link to the LRM with the Control Link\n         (id = 0). If this MIB variable is disabled the Host tries \n         to establish a session with the LRM through other links,\n         and if succeeds, it doesn't try to capture link 0.")
mibBuilder.exportSymbols("LANOPTICS-BRIDGE-OPTION-MIB", lanOpticsLMGRAgent=lanOpticsLMGRAgent, lanOpticsLMGRLinkID=lanOpticsLMGRLinkID, lanOptics=lanOptics, lanOpticsBridgeProxyAgent=lanOpticsBridgeProxyAgent, lanOpticsLMGRCaptCntrlLink=lanOpticsLMGRCaptCntrlLink)
