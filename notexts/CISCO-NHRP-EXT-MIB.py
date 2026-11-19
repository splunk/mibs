#
# PySNMP MIB module CISCO-NHRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NHRP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
nhrpServerNhcNbmaAddrType, nhrpServerInternetworkAddrType, nhrpServerNbmaAddrType, nhrpCacheNextHopInternetworkAddr, nhrpClientInternetworkAddr, nhrpClientRegUniqueness, nhrpClientNbmaSubaddr, nhrpClientNhsInUse, nhrpCacheNbmaAddr, nhrpServerNbmaSubaddr, nhrpClientNhsNbmaAddr, nhrpServerNhcNbmaAddr, nhrpClientInternetworkAddrType, nhrpServerNbmaAddr, nhrpClientNbmaAddrType, nhrpClientStatEntry, nhrpCacheNbmaAddrType, nhrpServerNhcNbmaSubaddr, nhrpServerNhcInUse, nhrpCacheNbmaSubaddr, nhrpServerInternetworkAddr, nhrpServerIndex, nhrpClientIndex, nhrpClientNbmaAddr, nhrpClientNhsNbmaAddrType, nhrpServerStatEntry, nhrpClientNhsInternetworkAddrType, nhrpServerNhcInternetworkAddrType, nhrpServerNhcInternetworkAddr, nhrpCacheType, nhrpServerNhcPrefixLength, nhrpClientNhsInternetworkAddr, nhrpClientNhsNbmaSubaddr, nhrpClientHoldTime, nhrpServerCacheUniqueness = mibBuilder.importSymbols("NHRP-MIB", "nhrpServerNhcNbmaAddrType", "nhrpServerInternetworkAddrType", "nhrpServerNbmaAddrType", "nhrpCacheNextHopInternetworkAddr", "nhrpClientInternetworkAddr", "nhrpClientRegUniqueness", "nhrpClientNbmaSubaddr", "nhrpClientNhsInUse", "nhrpCacheNbmaAddr", "nhrpServerNbmaSubaddr", "nhrpClientNhsNbmaAddr", "nhrpServerNhcNbmaAddr", "nhrpClientInternetworkAddrType", "nhrpServerNbmaAddr", "nhrpClientNbmaAddrType", "nhrpClientStatEntry", "nhrpCacheNbmaAddrType", "nhrpServerNhcNbmaSubaddr", "nhrpServerNhcInUse", "nhrpCacheNbmaSubaddr", "nhrpServerInternetworkAddr", "nhrpServerIndex", "nhrpClientIndex", "nhrpClientNbmaAddr", "nhrpClientNhsNbmaAddrType", "nhrpServerStatEntry", "nhrpClientNhsInternetworkAddrType", "nhrpServerNhcInternetworkAddrType", "nhrpServerNhcInternetworkAddr", "nhrpCacheType", "nhrpServerNhcPrefixLength", "nhrpClientNhsInternetworkAddr", "nhrpClientNhsNbmaSubaddr", "nhrpClientHoldTime", "nhrpServerCacheUniqueness")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNhrpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 680))
ciscoNhrpExtMIB.setRevisions(('2008-11-21 00:00',))
if mibBuilder.loadTexts: ciscoNhrpExtMIB.setLastUpdated('200811210000Z')
if mibBuilder.loadTexts: ciscoNhrpExtMIB.setOrganization('Cisco Systems, Inc.')
class CiscoNhrpErrorCode(TextualConvention, Integer32):
    reference = 'Sec.5.2.2, 5.2.4 and 5.2.7 of NHRP specification(RFC 2332) (April 1998)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 256))
    namedValues = NamedValues(("unrecogExtension", 1), ("loopDetected", 3), ("adminProhibited", 4), ("insufficientResources", 5), ("addressUnreachable", 6), ("protocolError", 7), ("sduSizeExceeded", 8), ("invalidExtension", 9), ("invalidResReply", 10), ("authFailure", 11), ("noAddressBinding", 12), ("bindingNotUnique", 13), ("uniqueInternetworkAddrRegd", 14), ("hopCountExceeded", 15), ("other", 256))

class CiscoNextHopDownReasonCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("administrative", 1), ("registrationFailure", 2), ("resolutionFailure", 3), ("purgeReceived", 4), ("normalExpiry", 5), ("external", 6), ("other", 7))

cneNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 0))
cneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1))
cneConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2))
cneGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1))
cneClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2))
cneServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3))
cneNotificationControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4))
cneNextHopDownReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 1), CiscoNextHopDownReasonCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cneNextHopDownReason.setStatus('current')
cneNHRPException = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 1, 2), CiscoNhrpErrorCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cneNHRPException.setStatus('current')
cneClientStatExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1), )
if mibBuilder.loadTexts: cneClientStatExtTable.setStatus('current')
cneClientStatExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1), )
nhrpClientStatEntry.registerAugmentions(("CISCO-NHRP-EXT-MIB", "cneClientStatExtEntry"))
cneClientStatExtEntry.setIndexNames(*nhrpClientStatEntry.getIndexNames())
if mibBuilder.loadTexts: cneClientStatExtEntry.setStatus('current')
cneClientStatRedirectRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cneClientStatRedirectRx.setStatus('current')
cneServerStatExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1), )
if mibBuilder.loadTexts: cneServerStatExtTable.setStatus('current')
cneServerStatExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1), )
nhrpServerStatEntry.registerAugmentions(("CISCO-NHRP-EXT-MIB", "cneServerStatExtEntry"))
cneServerStatExtEntry.setIndexNames(*nhrpServerStatEntry.getIndexNames())
if mibBuilder.loadTexts: cneServerStatExtEntry.setStatus('current')
cneServerStatRedirectTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cneServerStatRedirectTx.setStatus('current')
cneNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 680, 1, 4, 1), Bits().clone(namedValues=NamedValues(("nextHopRegServerUp", 0), ("nextHopRegServerDown", 1), ("nextHopRegClientUp", 2), ("nextHopRegClientDown", 3), ("nextHopPeerUp", 4), ("nextHopPeerDown", 5), ("rateLimitExceeded", 6))).clone(namedValues=NamedValues(("nextHopRegServerUp", 0), ("nextHopRegServerDown", 1), ("nextHopRegClientUp", 2), ("nextHopRegClientDown", 3), ("rateLimitExceeded", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cneNotifEnable.setStatus('current')
cneNotifNextHopRegServerUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 1)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"), ("NHRP-MIB", "nhrpClientNhsNbmaAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"), ("NHRP-MIB", "nhrpClientHoldTime"), ("NHRP-MIB", "nhrpClientRegUniqueness"), ("NHRP-MIB", "nhrpClientNhsInUse"))
if mibBuilder.loadTexts: cneNotifNextHopRegServerUp.setStatus('current')
cneNotifNextHopRegServerDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 2)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddrType"), ("NHRP-MIB", "nhrpClientNhsInternetworkAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaAddrType"), ("NHRP-MIB", "nhrpClientNhsNbmaAddr"), ("NHRP-MIB", "nhrpClientNhsNbmaSubaddr"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopRegServerDown.setStatus('current')
cneNotifNextHopRegClientUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 3)).setObjects(("NHRP-MIB", "nhrpServerInternetworkAddrType"), ("NHRP-MIB", "nhrpServerInternetworkAddr"), ("NHRP-MIB", "nhrpServerNbmaAddrType"), ("NHRP-MIB", "nhrpServerNbmaAddr"), ("NHRP-MIB", "nhrpServerNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"), ("NHRP-MIB", "nhrpServerNhcNbmaAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcPrefixLength"), ("NHRP-MIB", "nhrpServerNhcInUse"), ("NHRP-MIB", "nhrpServerCacheUniqueness"))
if mibBuilder.loadTexts: cneNotifNextHopRegClientUp.setStatus('current')
cneNotifNextHopRegClientDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 4)).setObjects(("NHRP-MIB", "nhrpServerInternetworkAddrType"), ("NHRP-MIB", "nhrpServerInternetworkAddr"), ("NHRP-MIB", "nhrpServerNbmaAddrType"), ("NHRP-MIB", "nhrpServerNbmaAddr"), ("NHRP-MIB", "nhrpServerNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddrType"), ("NHRP-MIB", "nhrpServerNhcInternetworkAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaAddrType"), ("NHRP-MIB", "nhrpServerNhcNbmaAddr"), ("NHRP-MIB", "nhrpServerNhcNbmaSubaddr"), ("NHRP-MIB", "nhrpServerNhcPrefixLength"), ("NHRP-MIB", "nhrpServerCacheUniqueness"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopRegClientDown.setStatus('current')
cneNotifNextHopPeerUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 5)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"), ("NHRP-MIB", "nhrpCacheNbmaAddrType"), ("NHRP-MIB", "nhrpCacheNbmaAddr"), ("NHRP-MIB", "nhrpCacheNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheType"))
if mibBuilder.loadTexts: cneNotifNextHopPeerUp.setStatus('current')
cneNotifNextHopPeerDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 6)).setObjects(("NHRP-MIB", "nhrpClientInternetworkAddrType"), ("NHRP-MIB", "nhrpClientInternetworkAddr"), ("NHRP-MIB", "nhrpClientNbmaAddrType"), ("NHRP-MIB", "nhrpClientNbmaAddr"), ("NHRP-MIB", "nhrpClientNbmaSubaddr"), ("NHRP-MIB", "nhrpCacheNextHopInternetworkAddr"), ("NHRP-MIB", "nhrpCacheNbmaAddrType"), ("NHRP-MIB", "nhrpCacheNbmaAddr"), ("NHRP-MIB", "nhrpCacheNbmaSubaddr"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"), ("CISCO-NHRP-EXT-MIB", "cneNHRPException"))
if mibBuilder.loadTexts: cneNotifNextHopPeerDown.setStatus('current')
cneNotifRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 680, 0, 7)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: cneNotifRateLimitExceeded.setStatus('current')
cneCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1))
cneGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2))
cneCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 1, 1)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotificationControlGroup"), ("CISCO-NHRP-EXT-MIB", "cneGeneralNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneGeneralGroup"), ("CISCO-NHRP-EXT-MIB", "cneClientNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneServerNotificationGroup"), ("CISCO-NHRP-EXT-MIB", "cneClientGroup"), ("CISCO-NHRP-EXT-MIB", "cneServerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneCompliance = cneCompliance.setStatus('current')
cneGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 1)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNHRPException"), ("CISCO-NHRP-EXT-MIB", "cneNextHopDownReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneGeneralGroup = cneGeneralGroup.setStatus('current')
cneClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 2)).setObjects(("CISCO-NHRP-EXT-MIB", "cneClientStatRedirectRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneClientGroup = cneClientGroup.setStatus('current')
cneServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 3)).setObjects(("CISCO-NHRP-EXT-MIB", "cneServerStatRedirectTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneServerGroup = cneServerGroup.setStatus('current')
cneNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 4)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneNotificationControlGroup = cneNotificationControlGroup.setStatus('current')
cneGeneralNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 5)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifRateLimitExceeded"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopPeerDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneGeneralNotificationGroup = cneGeneralNotificationGroup.setStatus('current')
cneClientNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 6)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegServerDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneClientNotificationGroup = cneClientNotificationGroup.setStatus('current')
cneServerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 680, 2, 2, 7)).setObjects(("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientUp"), ("CISCO-NHRP-EXT-MIB", "cneNotifNextHopRegClientDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cneServerNotificationGroup = cneServerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NHRP-EXT-MIB", cneServerStatRedirectTx=cneServerStatRedirectTx, cneServerGroup=cneServerGroup, cneClientObjects=cneClientObjects, cneGroups=cneGroups, cneClientGroup=cneClientGroup, cneClientStatExtEntry=cneClientStatExtEntry, cneServerObjects=cneServerObjects, cneNotifNextHopPeerUp=cneNotifNextHopPeerUp, cneGeneralGroup=cneGeneralGroup, cneNotifs=cneNotifs, CiscoNextHopDownReasonCode=CiscoNextHopDownReasonCode, cneGeneralObjects=cneGeneralObjects, cneNotifEnable=cneNotifEnable, cneNotifNextHopRegServerDown=cneNotifNextHopRegServerDown, cneNHRPException=cneNHRPException, PYSNMP_MODULE_ID=ciscoNhrpExtMIB, cneCompliances=cneCompliances, ciscoNhrpExtMIB=ciscoNhrpExtMIB, cneNotifNextHopRegClientUp=cneNotifNextHopRegClientUp, cneCompliance=cneCompliance, cneServerStatExtEntry=cneServerStatExtEntry, cneNotifNextHopRegServerUp=cneNotifNextHopRegServerUp, cneClientStatRedirectRx=cneClientStatRedirectRx, cneNotificationControlObjects=cneNotificationControlObjects, cneNotifNextHopRegClientDown=cneNotifNextHopRegClientDown, cneServerStatExtTable=cneServerStatExtTable, cneNotifRateLimitExceeded=cneNotifRateLimitExceeded, cneObjects=cneObjects, cneServerNotificationGroup=cneServerNotificationGroup, cneNextHopDownReason=cneNextHopDownReason, cneClientNotificationGroup=cneClientNotificationGroup, cneNotifNextHopPeerDown=cneNotifNextHopPeerDown, cneClientStatExtTable=cneClientStatExtTable, cneGeneralNotificationGroup=cneGeneralNotificationGroup, CiscoNhrpErrorCode=CiscoNhrpErrorCode, cneNotificationControlGroup=cneNotificationControlGroup, cneConform=cneConform)
